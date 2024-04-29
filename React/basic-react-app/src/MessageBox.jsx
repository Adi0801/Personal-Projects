import "./MessageBox.css"


// eslint-disable-next-line react/prop-types
function MessageBox({username , TextColor}){
    let styles={color:TextColor};
    return (
        <div className="Product" style={styles}>
            <h1 style={styles}>Hello {username}</h1>
        </div>
    )
}

export default MessageBox;