
Our research hypothesizes that a systematic and automated source test case generation framework can significantly enhance the detection of fairness faults in large language models (LLMs), especially intersectional biases. To test this, we developed GenFair and compared it against template-based and grammar-based (ASTRAEA) methods. We generated test cases using 15 manually designed templates, applied structured transformations, and evaluated the outputs of GPT-4.0 and LLaMA-3.0 under metamorphic relations (MRs). Fairness violations were identified when the tone or content changed unjustifiably between source and follow-up responses. GenFair demonstrated superior fault detection rates (FDR), higher syntactic and semantic diversity, and better coherence scores compared to the baselines. These results indicate that GenFair is more effective at uncovering subtle and intersectional biases, making it a robust tool for fairness testing in real-world LLM applications.

To use the Tool (GenFair):
1) Open Testcase_generation.py and execute the file to generate test cases.
2) Open the python file and put the input prompt file at the end of the file.
3) The input prompt file is provided inside MR Directory. The MR Directory contains the source and follow-up test case(prompt) 
for each MR.
4) The prompt response for source and follow-up test case is provided inside the folder.

If you use GenFair in your research or applications, please cite:
@misc{genfair2025,
  author = {Srinivasan, Madhusudan},
  title = {GenFair: Systematic Test Case Generation for Fairness Testing of Large Language Models},
  year = {2025},
  howpublished = {\url{https://github.com/ST-Lab-Srinivasan/GenFair}},
  note = {GitHub repository}
}
