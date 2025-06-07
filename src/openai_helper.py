"""Helper utilities for calling the OpenAI API."""

import os
import time
import logging
from dotenv import load_dotenv
from openai import OpenAI
from src.api_logger import log_openai_usage
from src.agents_logger import log_agent_action

# Configure a basic logger for TrendSpire
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)

load_dotenv()

_client = None


def _get_client() -> OpenAI:
    """Create the OpenAI client on first use."""
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        _client = OpenAI(api_key=api_key)
    return _client

# Rough USD cost per 1K tokens for supported models
MODEL_COST_PER_1K = {
    "gpt-3.5-turbo": 0.002,
}


def _estimate_cost(model: str, total_tokens: int) -> float:
    price = MODEL_COST_PER_1K.get(model, 0)
    return (total_tokens / 1000) * price

def ask_openai(prompt: str, model="gpt-3.5-turbo", temperature=0.5, max_tokens=1280) -> str:
    logger.info("\n----- OpenAI Request -----")
    logger.info(f"Model: {model} | Temperature: {temperature} | Max tokens: {max_tokens}")
    logger.info("Prompt:\n" + prompt)

    start = time.time()
    client = _get_client()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    elapsed = time.time() - start

    content = response.choices[0].message.content.strip()
    finish_reason = response.choices[0].finish_reason
    usage = response.usage
    if usage:
        cost = _estimate_cost(model, usage.total_tokens)
        logger.info(
            f"Tokens: prompt={usage.prompt_tokens} completion={usage.completion_tokens} "
            f"total={usage.total_tokens}"
        )
        logger.info(f"Estimated cost: ${cost:.6f}")
        log_openai_usage(model, usage.prompt_tokens, usage.completion_tokens, cost)
    else:
        logger.info("Token usage unavailable")
    if finish_reason and finish_reason != "stop":
        logger.warning(f"Response truncated (finish_reason={finish_reason})")
    else:
        logger.info(f"Finish reason: {finish_reason}")
    logger.info(f"Elapsed time: {elapsed:.2f}s")
    logger.info("Response:\n" + content)
    logger.info("----- End Request -----\n")
    log_agent_action("PromptGeneratorAgent", f"OpenAI request complete in {elapsed:.2f}s")

    return content
