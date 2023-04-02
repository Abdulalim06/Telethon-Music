import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = "6078033071:AAHPH2zQWFc34sg7t4cqlNDMMmaZiKkU1NM")
    STRING_SESSION = 1BVtsOJoBu5jVgkeIwIARAx5ZjyZFgGeWXsffb0cKiUFQ6DuIOZqe70xFmExV3v49LvORMNuh6d9z8yJopMQBQ-PZdkQ1saJKbcDIdSm2bkgh8_Svllfbs_VjcpaELtZUNZ7S1oQJ09bTFafz8QQ388NKqWVML3OLnSSdM2ehmHCxpe2CI1xy42JXETq1raGrUPCpFJ3oAq4TJ74eZTDurlcFqm8U9RetEhGmzfJ_dLHymWGRC5WWIZ7UzgycqvJN-teRqJjIgz_ttscdZG59GHweOBwWAqtvxDt5G17_sLuyN8Som7X2rra5SanWxqgDCG5lXt92ee7GWDomF5Cf--UJHqkP5O0=", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
