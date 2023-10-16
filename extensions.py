from maltego_trx.decorator_registry import TransformRegistry, TransformSet

registry = TransformRegistry(
        owner="Kodama Chameleon",
        author="Kodama <contact@kodamaChameleon.com>",
        host_url="https://transforms.acme.com",
        seed_ids=["SumoSearch"]
)

# The rest of these attributes are optional

sumoMaltego_set = TransformSet("SumoSearch", "SumoSearch Transforms")

# metadata
registry.version = "0.1"

# global settings
# from maltego_trx.template_dir.settings import api_key_setting
# registry.global_settings = [api_key_setting]

# transform suffix to indicate datasource
# registry.display_name_suffix = " [ACME]"

# reference OAuth settings
# registry.oauth_settings_id = ['github-oauth']
