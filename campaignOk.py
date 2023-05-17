from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv(find_dotenv())

def check_campaign(user_input):
    extract_result = extract_parameter(user_input)

    start_index = extract_result.index("[")
    end_index = extract_result.index("]")
    values = extract_result[start_index+1:end_index].split(",")
    params = [value.strip() for value in values]
    
    result = is_campaign_ok(params)

    return result


def extract_parameter(user_input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)    

    python_code = '''
        def is_campaign_ok(audience, campaign_duration, cpc, budget):
            calculation = ((audience * 0.46) * cpc * 0.015) * campaign_duration

            if calculation > budget:
                result = "YES"
            else:
                result = "NO"
        return result
    '''
    
    template = """
    
    You are a helpful assistant that show the result of python code.
    
    Your goal is to extract the parameter from user's input to use it as a parameter of the given python code.
        
    Start your reply in this format: "parameters: [200000, 10, 10, 1000000]"
    
    And then proceed with the reply on a new line.

    And if there's previous chat, append the previous chat in the end.
        
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = """
    

    Here's the python code : {python_code}.


    Here's the user input that you should extract parameters for the python code: {user_input}.
    
    """
    
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, python_code=python_code)

    return response

def is_campaign_ok(params):
    #English
    audience, campaign_duration, cpc, budget = map(int, params)
    calculation = ((audience * 0.46) * cpc * 0.015) * campaign_duration

    # result = f"""
    
    # Params [audience, campaign_duration, cpc, budget] are {params}. 
    
    # """

    # if calculation > budget:
    #     result += f"""
        
    # Calculation({calculation}) is greater than budget({budget}). The answer is YES
        
    # """
    # else:
    #     result += f"""
        
    # Calculation({calculation}) is less than budget({budget}). The answer is NO
        
    # """
        
    #Korean
    result = f"""
    
    모수, 캠페인 기간, cpc, 예산 : {params} . 
    
    """

    if calculation > budget:
        result += f"""
        
    대입 결과({calculation})가 예산({budget})보다 크기 때문에 집행이 "가능"합니다.
        
    """
    else:
        result += f"""
        
    대입 결과({calculation})가 예산({budget})보다 작기 때문에 집행이 "불가"합니다.
        
    """
    
    return result
