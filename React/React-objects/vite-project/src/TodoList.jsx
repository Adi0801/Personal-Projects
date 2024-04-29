import { useState } from "react";

export default function TodoList(){
    let[todos,settodos]=useState(["sample task"])
    let[newtodos,setnewtodos]=useState("");

    let newNew
    return(
        <div>
        <input placeholder="add a task" value={newtodos} />
        <button>Add Task</button>
        <br />
        <br />
        <br />
        <hr />
        <h1>To-Do List</h1>
        <ul>
           <li>{todos}</li> 
        </ul>
        </div>
    );
}