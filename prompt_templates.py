rater_identity_template_text_1 = """You might need to know that the target learners of this task are the Chinese senior high school EFL learners with an average of lower-intermediate level of English proficiency. Please imagine you are their English teacher when you score their writing samples for assignments by considering both acknowledging students’ highlights in their writing performance while also identifying room for improvement."""

rater_identity_template_text_2 = """The story continuation task is adopted in the National Matriculation English Test in China, which is a high-stakes screening test to select candidates for the university enrollment. Now, suppose you are a rater for the NMET, your ratings of the students’ continuation texts should be able to discriminate among students of different writing proficiency and be self-consistent in order to be fair. You need to stick to the rating rubrics strictly so that the ratings are readily interpretable by users of the test scores."""

task_description_template_text = """The story continuation task gives learners an unended story and asks them to continue it to make the story complete and coherent. This task aims to promote learners’ understanding of the given text and motivates them to align with the context and the language. The alignment effect thus couple language comprehension and production tightly to promote language development. """

assessment_criteria_template_text = """
The assessment of the continuation text by learners are centered around three dimensions, namely content and logical coherence, vocabulary and grammatical structure, and organization and cohesion. 

The rating rubrics are given below.
Dimension 1: Content and logical coherence
Fifth Level (21-25 points): Creates rich and well-structured content, demonstrating logical coherence and a high degree of integration with the original context.  
Fourth Level (16-20 points): Creates relatively rich and reasonable content, demonstrating comparably logical coherence and a relatively high degree of integration with the original context.
Third Level (11-15 points): Creates basically reasonable content, demonstrating some logical coherence and a basic level of integration with the original context. 
Second Level (6-10 points): Contains significant problems in content or logic, with incomplete continuation and a certain degree of disconnection from the original context. 
First Level (1-5 points): Contains significant problems in content or logic, or partially copies content from the original text, with incomplete continuation and a basic disconnection from the original context. 
Zero Score (0 points): No response provided; the written content is too minimal or illegible to evaluate, or the written content is entirely copied from the original text or completely unrelated to the given task.

Dimension 2: Vocabulary and grammatical structure
Fifth Level (21-25 points): Uses diverse and appropriate vocabulary and grammatical structures, with possibly a few minor errors that do not hinder comprehension. 
Fourth Level (16-20 points): Uses relatively diverse and appropriate vocabulary and grammatical structures, with some minor errors that do not significantly affect comprehension. 
Third Level (11-15 points): Uses simple vocabulary and grammatical structures, with some errors or inappropriate usage that do not significantly hinder comprehension.
Second Level (6-10 points): Uses limited vocabulary and monotonous grammatical structures, with numerous errors that hinder comprehension.  
First Level (1-5 points): Uses limited vocabulary and monotonous grammatical structures, with numerous errors that seriously hinder comprehension.  
Zero Score (0 points): No response provided; the written content is too minimal or illegible to evaluate, or the written content is entirely copied from the original text or completely unrelated to the given task.

Dimension 3: Organization and cohesion
Fifth Level (21-25 points): Effectively employs cohesive devices between sentences, maintaining a clear overall structure and coherent meaning. 
Fourth Level (16-20 points): Uses cohesive devices between sentences relatively effectively, resulting in a relatively clear overall structure and coherent meaning. 
Third Level (11-15 points): Uses cohesive devices between sentences to a basic extent, resulting in a basic overall structure and coherent meaning. 
Second Level (6-10 points): Fails to effectively use cohesive devices between sentences, resulting in an unclear overall structure and incoherent meaning. 
First Level (1-5 points): Almost no use of cohesive devices, resulting in an unclear overall structure and incoherent meaning. 
Zero Score (0 points): No response provided; the written content is too minimal or illegible to evaluate, or the written content is entirely copied from the original text or completely unrelated to the given task.

When assessing the overall quality of a story continuation text, especially in an educational context where English is being learned as a foreign language, it's important to consider how each of the three dimensions—content and logical coherence, vocabulary and grammatical structure, and organization and cohesion—contributes to effective communication and storytelling. Here's a general approach to weighing each dimension:
Content and Logical Coherence (40%)
This dimension is crucial because it evaluates the essence of the story continuation: how well the new text integrates with the original prompt and maintains a logical flow. Rich, imaginative content that demonstrates understanding and builds on the original story in a coherent way is fundamental. This dimension ensures that the story is engaging and meaningful.
Vocabulary and Grammatical Structure (30%)
Vocabulary richness and grammatical accuracy are key to expressing ideas clearly and effectively. This dimension assesses the learner's language proficiency, including their ability to use a range of vocabulary appropriately and to construct sentences that are grammatically correct. While minor errors that don't impede comprehension might be overlooked, frequent mistakes or limited vocabulary can significantly affect the clarity and impact of the story.
Organization and Cohesion (30%)
A well-organized text with clear cohesion between sentences and paragraphs makes the story easy to follow and enhances its overall impact. This dimension looks at the use of transitional phrases, paragraphing, and the logical arrangement of ideas to ensure that the narrative flows smoothly. Effective organization and cohesion contribute to the readability of the text and the audience's understanding and enjoyment.

Each dimension plays a vital role in the overall quality of the continuation text. However, content and logical coherence is slightly more weighted because it directly impacts the narrative's effectiveness and engagement level. Vocabulary and grammatical structure, and organization and cohesion are equally important but serve more as supporting elements that enhance the delivery of the content. This weighting can vary depending on specific educational objectives or assessment criteria, but it offers a balanced approach to evaluating a learner's storytelling and language skills."""

Holistic_rating_template_text = """Please give a holistic score (points not level) which evaluates the overall quality of the continuation text considering all three dimensions. Note that only a holistic score is needed for each continuation text without any comments."""

Analytical_rating_template_text = """
Please provide analytical scores on each of the dimensions in order to give learners diagnostic information about their writing performance.
When providing the scores, please use the following format: 
Content and logical coherence:
Vocabulary and grammatical structure:
Organization and cohesion:"""

user_message_text1 = """
Please read the input text to be continued by the learner.

{text}

Please note that the first sentences for paragraphs in the continuation text are given for the learners to guide their writing:

{guide}

Now the following is the learner's work:

{learner_work}
"""

user_message_text2 = """
Please read the input text to be continued by the learner.

{text}

Please note that the first sentences for paragraphs in the continuation text are given for the learners to guide their writing:

{guide}
"""

feedback_suggestion_text = """Please give detailed comments and suggestions on each of the three dimensions which will help learners improve their continuation text. Please make the feedback constructive, by providing very specific suggestions while also acknowledging the effort and creativity involved in the continuation attempt.

Based on the suggestions, please provide a revised version that is adaptive to the learner's language proficiency as demonstrated in their continuation writing (that is, the language in the revised version is better to be close to or a little more sophisticated than that in the learner’s output text) and highlight the major revisions. In the revised version, please keep the first sentence of both paragraphs intact ({guide_for_feedback}) and improve the continuation in response to the suggestions provided. Please also highlight all the revisions made and explain why."""

suggestion_dimension_text_1 = """Now please focus on the content and logical coherence dimension and provide detailed comments and suggestions which will help learners improve their continuation text particularly in this dimension. 
Your comment might revolve around the following aspects, namely whether the generated contents well aligns with the original context and conform to the reality and world knowledge, whether the development of logic is reasonable and coherent, whether the overall emotions and values are consistent with the original text and so on. Enumerate merits with specific references to the student’s writing, point out all the problems identified in the student’s writing, explain reasons and provide suggestions for revisions."""

suggestion_dimension_text_2 = """Now please focus on the Vocabulary and Grammar dimension and provide detailed comments and suggestions which will help learners improve their continuation text particularly in this dimension. 
Your comment might revolve around the following aspects, namely whether there are spelling mistakes, whether the vocabulary, phrases and collocations are accurate, covering a considerable range and are well-chosen for the context, whether the syntactic structures are correctly used and whether diversified sentence patterns are used for effective meaning construction.Enumerate merits with specific references to the student’s writing, point out all the problems identified in the student’s writing, explain reasons and provide suggestions for revisions."""

suggestion_dimension_text_3 = """Now please focus on the Organization and cohesion dimension and provide detailed comments and suggestions which will help learners improve their continuation text particularly in this dimension. 
Your comment might revolve around the following aspects, namely whether the continuation text is proper organized and structured and whether effective cohesive devices are employed. Enumerate merits with specific references to the student’s writing, point out all the problems identified in the student’s writing, explain reasons and provide suggestions for revisions."""

compare_template_text = """
I am a senior high school student in China. I have revised my continuation text following the suggestions provided. Here are the two versions:
Original version: {original_version}
Revised version：{revised_version}
Can you please compare the two versions and comment on whether the revisions in the revised version can help enhance the overall quality and score. Highlight and analyze reasons for proper revisions that are conducive to the improvement of the continuation text while pointing out and give further revision suggestions for those that still need improvement."""

provide_model_text = """I am a senior high school student in China. I have completed the writing continuation task. Now please provide a model text that I can learn from. In the model text, don’t forget to keep the first sentence of the two continued paragraphs intact ({guide_provided}) 
Please also provide an analysis of how the model text is well aligned with the original text in terms of the content, language and cohesion."""

assistance_text = """I am a senior high school student in China. I am going to complete this writing continuation task. I need some assistance when I am planning for writing. Please do not provide a continuation text directly because I want to write independently to improve my writing skills. But you may help me by giving some guidance on how to generate contents that are well-aligned with the given text. You may also highlight the essential story line and the important clues that might be important for writing a continuation text. You may also highlight some vocabulary, phrases or sentence patterns that I might use in my continuation text."""