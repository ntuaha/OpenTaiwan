# OpenTaiwan
A plugin to provide Taiwan government information on chatGPT.

This plugin allows users to access various information about the Taiwan from the official government open data portal using chatGPT, a conversational AI system. Users can ask questions or request topics related to Taiwan's history, politics, economy, culture, science, education, and more. The plugin will use chatGPT to generate natural language responses based on the relevant web pages from the government portal. The plugin aims to provide accurate, up-to-date, and comprehensive information about Taiwan to chatGPT users.
## Features (TODO)

- Natural language understanding
- Multiple domains: You can query information from different domains, such as COVID-19 statistics, visa requirements, public transportation, etc.
- Multilingual support: You can use either English or Chinese to interact with the plugin. The plugin will automatically detect your language preference and respond accordingly.

## Prerequisites
- You need to have chatGPT plugin installed and activated on your open.ai account.
- You need to have python 3.8 or higher installed on your machine.

## Getting Started for Developers

1. Open terminal and use the following command to start localhost api on port 3333

```bash
pip install -r requirements.txt
python api.py --reload
```
2. Go to chatGPT plugin store and click on Develop your own plugin, and enter localhost:3333
3. Enable TaiwanOpen plugin (currently up to 3 plugins can be used at the same time in chatGPT)
4. Have Fun!

## Getting Started for Users

To use the plugin, you need to activate it in chatGPT. Then, you can start asking questions about Taiwan government information. For example:

- Shimen Reservoir Water Level Change Trend Chart
- 全台水庫狀況如何?

The plugin will help chatGPT to answer your questions using the available data sources. If it cannot find an answer or if your question is out of scope, it will let you know and suggest other possible sources of information.

## What's Next

- add more various data from Taiwan Open Government Data
    1. finance
    2. traffic
    3. weather
    4. ... and so on

## Feedback

We appreciate your feedback and suggestions for improving this plugin. You can report any issues or feature requests on the GitHub issue tracker. You can also contact us by email at ntuaha@gmail.com.

## Reference documents
- For more details on how to use chatGPT and its plugins, please refer to [Getting started on CHAT PLUGINS in open.ai](https://platform.openai.com/docs/plugins/getting-started).

## Support
Donation Link: https://www.buymeacoffee.com/donateaha

