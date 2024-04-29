function handleFormSubmit(){
    console.log("form was submitted");
}

export default function Form(){
    return(
        <form action="">
            <input placeholder="write something" />
            <button onClick={handleFormSubmit}>Submit</button>
        </form>
    )
}