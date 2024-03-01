from diceutils.logging import Logger

import pytest


@pytest.fixture
def logger():
    return Logger(":memory:")


def test_init(logger):
    logger.rescue()


def test_add(logger):
    logger.add(
        "0",
        0,
        user_id="0",
        user_role="KP",
        data=[
            {
                "type": "text",
                "data": "test data",
            }
        ],
        message_sequence="xxx",
    )
    logger.rescue()


def test_get(logger):
    logger.add(
        "0",
        0,
        user_id="0",
        user_role="KP",
        data=[
            {
                "type": "text",
                "data": "test data",
            }
        ],
        message_sequence="xxx",
    )
    assert isinstance(logger.load("0", 0), list)
    assert logger.load("0", 0)[0]["user_id"] == "0"
    assert logger.load("0", 0)[0]["user_role"] == "KP"


def test_remove(logger):
    logger.add(
        "0",
        0,
        user_id="0",
        user_role="KP",
        data=[
            {
                "type": "text",
                "data": "test data",
            }
        ],
        message_sequence="xxx",
    )
    assert logger.load("0", 0) != []
    logger.remove("0", 0, "xxx")
    assert logger.load("0", 0) == []
    logger.rescue()


def test_clear(logger):
    logger.add(
        "0",
        0,
        user_id="0",
        user_role="KP",
        data=[
            {
                "type": "text",
                "data": "test data",
            }
        ],
        message_sequence="xxx",
    )
    logger.clear("0", 0)
    assert logger.load("0", "0") == []
    assert logger.loadall() == {}
    logger.rescue()
