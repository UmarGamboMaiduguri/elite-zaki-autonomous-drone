from elite_zaki.networking.receiver import TelemetryReceiver


def test_receiver_accepts_valid_signed_payload():
    receiver = TelemetryReceiver(secret=b"test-secret")

    payload = b'{"node_id":"zaki-01","status":"ok"}'
    signature = receiver.sign(payload)

    result = receiver.receive(payload, signature)

    assert result.accepted is True
    assert result.reason == "valid"


def test_receiver_rejects_invalid_signature():
    receiver = TelemetryReceiver(secret=b"test-secret")

    payload = b'{"node_id":"zaki-01","status":"ok"}'
    invalid_signature = "invalid-signature"

    result = receiver.receive(payload, invalid_signature)

    assert result.accepted is False
    assert result.reason == "invalid_signature"


def test_receiver_rejects_stale_payload():
    receiver = TelemetryReceiver(
        secret=b"test-secret",
        max_age_seconds=1,
    )

    payload = b'{"node_id":"zaki-01","status":"ok"}'
    signature = receiver.sign(payload)

    result = receiver.receive(
        payload,
        signature,
        timestamp=0,
    )

    assert result.accepted is False
    assert result.reason == "stale"
