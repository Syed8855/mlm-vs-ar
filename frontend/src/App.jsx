import { useState } from 'react'
import "./App.css";

import PromptInput from './components/PromptInput';
import RunButton from './components/RunButton';
import ResultBox from './components/ResultBox'; 
function App() {
  const [prompt, setPrompt] = useState('');
  const [result, setResult] = useState('');
  function handleRun(){
    setResult(prompt);
  }

  return (
    <div className="Container">
      <h1>MLM vs AR Benchmark</h1>
      <PromptInput prompt={prompt} setPrompt={setPrompt}/>
      <RunButton handleRun={handleRun}/>
      <ResultBox result={result}/>
    </div>
  );
}

export default App;