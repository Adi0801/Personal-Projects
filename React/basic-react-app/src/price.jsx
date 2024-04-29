// eslint-disable-next-line react/prop-types
export default function Price({oldPrice,newPrice}){
    let oldstyles={
        textDecorationLine:"Line-through", //for line acrros old price
    }
    let newstyles={
        fontWeight:"bold",
    }

    let styles={
        backgroundColor:"yellow",
        height:"30px",
        borderBottomLeftRadious:"14px",
        borderBottomRightRadious:"14px",


    }
    return(
        <div style={styles} >
            <span style={oldstyles}>{oldPrice}</span>
            &nbsp;&nbsp;&nbsp; 
            <span style={newstyles}>{newPrice}</span>
        </div>
    );
}

//nbsp is non break spacing