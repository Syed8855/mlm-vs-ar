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
      const response = await fetch('http://localhost:5000/models');
      const data = await response.json();
      console.log(data);
      setResult(data.message);
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