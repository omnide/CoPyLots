import pynecone as pc

class CopylotsConfig(pc.Config):
    pass

config = CopylotsConfig(
    app_name="CoPyLots",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
