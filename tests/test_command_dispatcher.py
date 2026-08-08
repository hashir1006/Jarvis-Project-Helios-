from jarvis.core.command_dispatcher import CommandDispatcher
from jarvis.core.intent_parser import Intent


def test_dispatcher():

    dispatcher = CommandDispatcher()

    intent = Intent(
        action="status",
        target="explorer",
    )

    result = dispatcher.dispatch(intent)

    print(result)

    assert result.success is True
    assert result.message == "explorer is running."