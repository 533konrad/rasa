import os
import pkg_resources

DEFAULT_ENDPOINTS_PATH = "endpoints.yml"
DEFAULT_CREDENTIALS_PATH = "credentials.yml"
DEFAULT_CONFIG_PATH = "config.yml"
DEFAULT_DOMAIN_PATH = "domain.yml"
DEFAULT_ACTIONS_PATH = "actions"
DEFAULT_MODELS_PATH = "models"
DEFAULT_DATA_PATH = "data"
DEFAULT_RESULTS_PATH = "results"
DEFAULT_NLU_RESULTS_PATH = "nlu_comparison_results"
DEFAULT_REQUEST_TIMEOUT = 60 * 5  # 5 minutes

TEST_DATA_FILE = "test.md"
TRAIN_DATA_FILE = "train.md"
RESULTS_FILE = "results.json"
NUMBER_OF_TRAINING_STORIES_FILE = "num_stories.json"
PERCENTAGE_KEY = "__percentage__"

PACKAGE_NAME = "rasa"

CONFIG_SCHEMA_FILE = "nlu/schemas/config.yml"
DOMAIN_SCHEMA_FILE = "core/schemas/domain.yml"

DEFAULT_RASA_X_PORT = 5002
DEFAULT_RASA_PORT = 5005

DOCS_BASE_URL = "https://rasa.com/docs/rasa"
LEGACY_DOCS_BASE_URL = "http://legacy-docs.rasa.com"

FALLBACK_CONFIG_PATH = pkg_resources.resource_filename(
    __name__, "cli/default_config.yml"
)
CONFIG_MANDATORY_KEYS_CORE = ["policies"]
CONFIG_MANDATORY_KEYS_NLU = ["language", "pipeline"]
CONFIG_MANDATORY_KEYS = CONFIG_MANDATORY_KEYS_CORE + CONFIG_MANDATORY_KEYS_NLU

MINIMUM_COMPATIBLE_VERSION = "1.0.0rc1"

GLOBAL_USER_CONFIG_PATH = os.path.expanduser("~/.config/rasa/global.yml")

DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOG_LEVEL_RASA_X = "WARNING"
DEFAULT_LOG_LEVEL_LIBRARIES = "ERROR"
ENV_LOG_LEVEL = "LOG_LEVEL"
ENV_LOG_LEVEL_LIBRARIES = "LOG_LEVEL_LIBRARIES"
