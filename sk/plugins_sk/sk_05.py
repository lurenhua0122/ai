import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatCompletion
from IPython.display import display, Markdown

kernel = sk.Kernel()

useAzureOpenAI = False

if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_text_completion_service("azureopenai",AzureChatCompletion(deployment_name=deployment,api_key=api_key,endpoint=endpoint))
else:
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service("openai",OpenAIChatCompletion("gpt-3.5-turbo",api_key=api_key))

print("A Kernel is now ready.")



strengths = [ "Unique garlic pizza recipe that wins top awards","Owner trained in Sicily at some of the best pizzerias","Strong local reputation","Prime location on university campus" ]
weaknesses = [ "High staff turnover","Floods in the area damaged the seating areas that are in need of repair","Absence of popular calzones from menu","Negative reviews from younger demographic for lack of hip ingredients" ]

pluginsDirectory = "./plugins-sk"

pluginBT = kernel.import_semantic_skill_from_directory(pluginsDirectory, "BusinessThinking");

my_context = kernel.create_new_context()
my_context['input'] = 'makes pizzas'
my_context['strengths'] = ", ".join(strengths)
my_context['weaknesses'] = ", ".join(weaknesses)

costefficiency_result =  kernel.run_async(pluginBT["SeekCostEfficiency"], input_context=my_context)
costefficiency_str = str("### ✨ Suggestions for how to gain cost efficiencies\n" + str(costefficiency_result))
display(Markdown(costefficiency_str))

opportunities = [ "Untapped catering potential","Growing local tech startup community","Unexplored online presence and order capabilities","Upcoming annual food fair" ]
threats = [ "Competition from cheaper pizza businesses nearby","There's nearby street construction that will impact foot traffic","Rising cost of cheese will increase the cost of pizzas","No immediate local regulatory changes but it's election season" ]

pluginBT = kernel.import_semantic_skill_from_directory(pluginsDirectory, "BusinessThinking");

my_context = kernel.create_new_context()
my_context['input'] = 'makes pizzas'
my_context['strengths'] = ", ".join(strengths)
my_context['weaknesses'] = ", ".join(weaknesses)
my_context['opportunities'] = ", ".join(opportunities)
my_context['threats'] = ", ".join(threats)

bizstrat_result = await kernel.run_async(pluginBT["BasicStrategies"],input_context=my_context)
bizstrat_str = "## ✨ Business strategy thinking based on SWOT analysis\n"+str(bizstrat_result)
display(Markdown(bizstrat_str))