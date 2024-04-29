import { useState } from "react";

function init(){
    console.log("init is excuted");
    return Math.random();
}

export default function Counter(){
    // let [count, setCount]=useState(0);
    let [count, setCount]=useState(init);//take input by calling one time init

    function incCount(){
        // setCount(count+1);
        // console.log(count);

        //update counts as 0 3 6 9
        // setCount((currCount)=>{
        //     return currCount+1;
        // })
        // setCount((currCount)=>{
        //     return currCount+1;
        // })
        // setCount((currCount)=>{
        //     return currCount+1;
        // })

        // take random value from init
        setCount(count+1);
        console.log(count);
    }

    return(
        <div>
            <h3>Count={count}</h3>
            <button onClick={incCount}>Increase Count</button>
        </div>
    )
}