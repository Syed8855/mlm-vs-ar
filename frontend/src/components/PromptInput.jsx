function PromptInput({ prompt, setPrompt}) {
    return(<input
        type="text"
        value={prompt}
        placeholder="Enter prompt"
        onChange={(e)=>setPrompt(e.target.value)}
        />
    );
}
export default PromptInput;