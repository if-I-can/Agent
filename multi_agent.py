from mul_agent_depend import Crew
from mul_agent import Agent
from mul_agent_depend.tool import tool

@tool
def read_md(filename: str) -> str:
    """
    Reads an md file and returns its content.
    """
    with open(filename, "r") as f:
        return f.read()

@tool
def write_str_to_txt(text: str) -> str:
    """
    Writes the Q&A content to a text file.
    """
    print("write_str_to_txt", text)
    with open(
        "/home/zsl/Agent/test.txt", "w"
    ) as f:
        f.write(text)
    return "done"

with Crew() as crew:
    agent1 = Agent(
        name="Initial Question Generator",
        backstory="""You are a distinguished expert in fishery science and aquaculture education with extensive experience in knowledge assessment. 
        Your expertise includes:
        - Deep understanding of aquaculture systems and fish farming technology
        - Strong background in educational assessment design
        - Ability to create questions that test both theoretical knowledge and practical understanding
        
        Your role is to generate initial questions that:
        - Cover key concepts comprehensively
        - Range from fundamental principles to advanced applications
        - Connect theoretical knowledge with practical implications
        - Encourage critical thinking about aquaculture systems""",
        task_description="""Generate 5 professional questions based on the provided article, following these guidelines:
        1. Ensure questions span different cognitive levels (recall, comprehension, application, analysis)
        2. Focus on core concepts and their practical applications
        3. Include questions about both technical details and broader implications
        4. Maintain clear connection to the source material
        5. Consider both theoretical understanding and practical implementation
        content path :"/home/wch/3.8t_1/Workspace/wch/fish_llm/data/processed1/10 水产投喂系统构建/中文/202204 - 朱明 - 农业工程学报 - 鱼类养殖智能投喂方法研究进展.pdf/output.md"
        Each question should:
        - Be clearly worded and technically precise
        - Target specific learning objectives
        - Encourage deep understanding rather than surface-level recall""",
        task_expected_output="""Output exactly 5 questions that:
        - Are clearly numbered (1-5)
        - Use precise technical terminology
        - Are self-contained and unambiguous
        - Progress logically from fundamental to advanced concepts""",
        tools=[read_md]
    )

    agent2 = Agent(
        name="Question Enhancement Specialist",
        backstory="""You are an expert question quality analyst with dual expertise in fishery science and educational assessment. 
        Your specialties include:
        - Advanced question design methodology
        - Technical accuracy in aquaculture terminology
        - Educational assessment optimization
        - Cognitive level analysis
        
        Your role is to transform good questions into excellent ones through careful analysis and refinement.""",
        task_description="""Analyze and enhance the received questions through three structured reflection stages:

        STAGE 1 - TECHNICAL ANALYSIS:
        - Verify technical accuracy and terminology
        - Check alignment with source material
        - Identify any ambiguities or imprecisions
        - Assess coverage of key concepts
        
        STAGE 2 - PEDAGOGICAL ENHANCEMENT:
        - Optimize cognitive level distribution
        - Improve question clarity and focus
        - Enhance assessment effectiveness
        - Ensure appropriate difficulty progression
        
        STAGE 3 - FINAL REFINEMENT:
        - Fine-tune language for precision
        - Verify comprehensive topic coverage
        - Ensure logical question sequence
        - Validate technical accuracy""",
        task_expected_output="""Provide 5 enhanced questions that:
        - Demonstrate clear improvement from originals
        - Maintain technical precision
        - Show optimal cognitive level distribution
        - Form a coherent assessment set
        
        Include brief reflection notes on improvements made.""",
        use_reflection=True,
        reflection_steps=3
    )

    agent3 = Agent(
        name="Expert Answer Generator",
        backstory="""You are a highly qualified aquaculture scientist and educator with:
        - Extensive research experience in fish farming technologies
        - Deep understanding of aquaculture systems
        - Expertise in explaining complex concepts
        - Strong technical writing skills
        
        Your role is to provide comprehensive, accurate, and educational answers that:
        - Demonstrate deep subject knowledge
        - Connect theory with practical applications
        - Provide clear explanations
        - Reference relevant source material""",
        task_description="""Generate expert-level answers to the optimized questions based on the source material, ensuring:
        1. Technical Accuracy:
           - Use precise terminology
           - Provide accurate information
           - Maintain consistency with source material
        
        2. Comprehensiveness:
           - Cover all relevant aspects
           - Include supporting details
           - Connect to broader concepts
        
        3. Educational Value:
           - Explain complex concepts clearly
           - Include relevant examples
           - Highlight practical applications
           
           
        content path :"/home/wch/3.8t_1/Workspace/wch/fish_llm/data/processed1/10 水产投喂系统构建/中文/202204 - 朱明 - 农业工程学报 - 鱼类养殖智能投喂方法研究进展.pdf/output.md"
           """,
        task_expected_output="""Provide a Q&A set that:
        - Pairs each question with its comprehensive answer
        - Maintains consistent formatting
        - Uses technical language appropriately
        - Provides clear, educational explanations
        
        Format as:
        Q1: [Question]
        A1: [Comprehensive answer]
        
        [Continue for all questions]""",
        tools=[read_md]
    )
    agent4 = Agent(
        name="Fishery Content Translator",
        backstory="""You are a specialized translator in aquaculture and fishery science with:
        - Deep expertise in fishery and aquaculture terminology
        - Professional experience in technical translation
        - Strong understanding of Chinese aquaculture industry standards
        - Extensive knowledge of scientific writing in Chinese
        
        Your role is to translate the formatted Q&A content into precise, 
        professional Chinese while maintaining technical accuracy.""",
        task_description="""Translate the Q&A content into Chinese following these principles:
        1. Technical Accuracy:
           - Use standard Chinese aquaculture terminology
           - Maintain scientific precision
           - Ensure concept accuracy
        
        2. Language Quality:
           - Adopt professional Chinese scientific writing style
           - Ensure natural and fluid expression
           - Maintain appropriate formality level
        
        3. Content Integrity:
           - Preserve all technical details
           - Maintain the original structure
           - Ensure no information loss
        
        4. Final Review:
           - Verify translation accuracy
           - Check terminology consistency
           - Ensure readability for Chinese professionals""",
        task_expected_output="""输出格式化的中文问答内容：
        - 使用规范的水产养殖专业术语
        - 保持清晰的问答对应关系
        - 确保专业性和可读性
        
        格式要求：
        问题1：[中文问题]
        答案1：[中文答案]
        
        [依此类推]""",
        tools=[write_str_to_txt],
    )

    agent1 >> agent2 >> agent3 >> agent4

crew.plot()
crew.run()