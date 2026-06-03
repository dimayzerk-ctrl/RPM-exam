def test_open_app_action():
    cmd = {
        "action": "open_app",
        "app": "chrome"
    }

    assert cmd["action"] == "open_app"