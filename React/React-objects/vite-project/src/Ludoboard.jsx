import { useState } from "react";

export default function LudoBoard(){
    let[Move,setMove]=useState({blue:0,red:0,yellow:0,green:0});
    let[arr,SetArr]=useState(["no moves"]);

    let updateBlue=()=>{
        // Move.blue+=1;
        // console.log('moves.blue = $(Move.blue)');
        setMove((prevMoves)=>{
            return{
                ...prevMoves, blue:prevMoves.blue+1
            }
        }); 
        
        SetArr((prevArr)=>{return(
            [...prevArr,"blue moves"]
        )});
    };

    let updateYellow=()=>{
        // Move.blue+=1;
        // console.log('moves.blue = $(Move.blue)');
        setMove((prevMoves)=>{
            return{
                ...prevMoves, yellow:prevMoves.yellow +1
            }
        });   
    };

    let updateGreen=()=>{
        // Move.blue+=1;
        // console.log('moves.blue = $(Move.blue)');
        setMove((prevMoves)=>{
            return{
                ...prevMoves, green:prevMoves.green+1
            }
        });   
    };

    let updateRed=()=>{
        // Move.blue+=1;
        // console.log('moves.blue = $(Move.blue)');
        setMove((prevMoves)=>{
            return{
                ...prevMoves, red:prevMoves.red+1
            }
        });   
    };

    return(
        <div>
        <p>Game Begins</p>
        <p>{arr}</p>
        <div className="board">
            <p>Blue moves = {Move.blue} </p>
            <button style={{backgroundColor:"blue"}} onClick={updateBlue}>+1</button>
            <p>Yellow moves ={Move.yellow}</p>
            <button style={{backgroundColor:"yellow"}} onClick={updateYellow}>+1</button>
            <p>Green moves ={Move.green} </p>
            <button style={{backgroundColor:"green"}} onClick={updateGreen}>+1</button>
            <p>Red moves ={Move.red} </p>
            <button style={{backgroundColor:"red"}} onClick={updateRed}>+1</button>
        </div>
        </div>
    );
}