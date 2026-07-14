import { useState } from 'react'
import "./App.css";

import PromptInput from './components/PromptInput';
import RunButton from './components/RunButton';
import ResultBox from './components/ResultBox'; 
function App() {
  const [prompt, setPrompt] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  async function handleRun() {
    try{
      setLoading(true);
      const response = await fetch('http://localhost:8000/benchmark', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt : prompt }),
      });
      if (!response.ok) {
        throw new Error("Server error");
      }
      const data = await response.json();
      console.log(data);
      setResult(
        `Prompt: ${data.received_prompt}
        Status: ${data.status}`
      );
    }
    catch(error){
      setResult('Error occurred while fetching data');
    }
    finally{
      setLoading(false);
    }
  }
  return (
    <div className="Container">
      <h1>MLM vs AR Benchmark</h1>
      <PromptInput prompt={prompt} setPrompt={setPrompt}/>
      <RunButton handleRun={handleRun}/>
      <ResultBox 
        result={result}
        loading={loading}/>
    </div>
  );
}

export default App;