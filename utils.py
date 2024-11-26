from prompt_templates import rater_identity_template_text_1, rater_identity_template_text_2, \
    task_description_template_text, assessment_criteria_template_text, Holistic_rating_template_text,\
    Analytical_rating_template_text, user_message_text1, feedback_suggestion_text, suggestion_dimension_text_1,\
    suggestion_dimension_text_2, suggestion_dimension_text_3, compare_template_text, assistance_text,\
    provide_model_text, user_message_text2
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def rater(api_key, role, way, text, guide, learner_work):
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, base_url="https://api.aigc369.com/v1")
    system_template_text = task_description_template_text + "\n" + assessment_criteria_template_text
    if role == "High-School English teacher":
        system_template_text = system_template_text + "\n" + rater_identity_template_text_1
    else:
        system_template_text = system_template_text + "\n" + rater_identity_template_text_2

    if way == "Holistic":
        user_template_text = user_message_text1 + "\n" + Holistic_rating_template_text
    else:
        user_template_text = user_message_text1 + "\n" + Analytical_rating_template_text

    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', system_template_text),
            ('user', user_template_text)
        ]
    )
    chain = prompt | model
    result = chain.invoke(
        {
            "text": text,
            "guide": guide,
            "learner_work": learner_work
        }
    )
    return result.content


def feedback(api_key, dim, text, guide, learner_work):
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, base_url="https://api.aigc369.com/v1")
    system_template_text = task_description_template_text + "\n" + assessment_criteria_template_text
    if dim == "ALL":
        user_template_text = user_message_text1 + "\n" + feedback_suggestion_text
        prompt = ChatPromptTemplate.from_messages(
            [
                ('system', system_template_text),
                ('user', user_template_text)
            ]
        )
        chain = prompt | model
        result = chain.invoke(
            {
                "text": text,
                "guide": guide,
                "guide_for_feedback": guide,
                "learner_work": learner_work
            }
        )
        return result.content
    elif dim == "Content and Logical Coherence":
        user_template_text = user_message_text1 + "\n" + suggestion_dimension_text_1
    elif dim == "Vocabulary and Grammar":
        user_template_text = user_message_text1 + "\n" + suggestion_dimension_text_2
    elif dim == "Organization and Cohesion":
        user_template_text = user_message_text1 + "\n" + suggestion_dimension_text_3

    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', system_template_text),
            ('user', user_template_text)
        ]
    )

    chain = prompt | model
    result = chain.invoke(
        {
            "text": text,
            "guide": guide,
            "learner_work": learner_work
        }
    )
    return result.content


def compare(api_key, text, guide, original_version, revised_version):
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, base_url="https://api.aigc369.com/v1")
    system_template_text = task_description_template_text + "\n" + assessment_criteria_template_text
    user_template_text = user_message_text2 + "\n" + compare_template_text
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', system_template_text),
            ('user', user_template_text)
        ]
    )

    chain = prompt | model
    result = chain.invoke(
        {
            "text": text,
            "guide": guide,
            "original_version": original_version,
            "revised_version": revised_version
        }
    )
    return result.content


def assist(api_key, text, guide):
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, base_url="https://api.aigc369.com/v1")
    system_template_text = task_description_template_text + "\n" + assessment_criteria_template_text
    user_template_text = user_message_text2 + "\n" + assistance_text
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', system_template_text),
            ('user', user_template_text)
        ]
    )

    chain = prompt | model
    result = chain.invoke(
        {
            "text": text,
            "guide": guide,
        }
    )
    return result.content


def pro_model(api_key, text, guide):
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, base_url="https://api.aigc369.com/v1")
    system_template_text = task_description_template_text + "\n" + assessment_criteria_template_text
    user_template_text = user_message_text2 + "\n" + provide_model_text
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', system_template_text),
            ('user', user_template_text)
        ]
    )

    chain = prompt | model
    result = chain.invoke(
        {
            "text": text,
            "guide": guide,
            "guide_provided": guide
        }
    )
    return result.content
