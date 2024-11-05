<h1>Vendor Invoice Extraction Using LLM</h1>

<p>This project is an LLM system designed to upload invoices and extract essential details such as vendor name, invoice amount, date, and invoice number. It comprises a Streamlit front end, FastAPI backend, and Ollama endpoint for interaction with the LLM. Technologies used include Python and Langchain.</p>

<h2>Features</h2>
<ul>
    <li>Upload invoice in PDF format</li>
    <li>Extract vendor name, invoice amount, date, and invoice number from invoices</li>
    <li>User-friendly interface with Streamlit</li>
    <li>Fast and efficient API using FastAPI</li>
    <li>Seamless interaction with LLM through Ollama endpoint</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Python:</strong> Programming language</li>
    <li><strong>Langchain:</strong> Framework for building applications with LLMs</li>
    <li><strong>Streamlit:</strong> Front-end web application framework</li>
    <li><strong>FastAPI:</strong> Back-end web framework for building APIs</li>
    <li><strong>Ollama:</strong> Endpoint for interacting with the LLM</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/arav4450/Vendor-Invoice-Extraction-Using-LLM.git</code></pre>
    </li>
    <li>Change to the project directory:
    </li>
    <li>Create a new environment and install the required dependencies:
        <pre>
          <code>conda env create -f environment.yml</code>
          <code>conda activate env_name</code>
          <code>pip-compile dev.in</code>
          <code>pip-sync dev.txt</code>
        </pre>
    </li>
    <li>
      Download and install ollama: https://ollama.com/ and download required model by running the command from terminal
      <pre><code>ollama pull starling-lm:7b-alpha-q5_K_M</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Run the FastAPI server:
        <pre><code>uvicorn server_api:app --reload</code></pre>
    </li>
    <li>Launch the Streamlit app:
        <pre><code>streamlit run client.py</code></pre>
    </li>
    <li>Open your browser and navigate to the provided URL to use the application.</li>
</ol>


<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

