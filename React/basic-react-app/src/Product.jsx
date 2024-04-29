/* eslint-disable react/no-unescaped-entities */
/* eslint-disable no-unused-vars */
import "./Product.css";

// eslint-disable-next-line react/prop-types
// function Product({ title, price=1, features}) {
//     // eslint-disable-next-line react/prop-types, react/jsx-key
//     const list=features.map((features)=><li>{features}</li>)
//     return (
//         <div className="Product">
//             <h3>{title}</h3>
//             <h5>{price}</h5>
//             <p>{list}</p>
//             {/* <p>{features2}</p> */}
//         </div>
//     );
// }

// eslint-disable-next-line react/prop-types
// function Product({title, price=1}) {
//     // eslint-disable-next-line react/prop-types, react/jsx-key
    
//     //dynamic styling based upon some conditions--here based upon the condions backgroundcolor changed -this bg col is css but we have to write in jsx format to remove hypen
//     let styles={backgroundColor:price>30000?"yellow":""};
//     //condions in reacts -adding some element on the some conditions
//     return (
//         <div className="Product" style={styles}>
//             <h3>{title}</h3>
//             <h5>{price}</h5>
//             {price > 30000 && <p>"Discount of 5 %"</p>}
//         </div>
//     );
// }

//activity-2
import Price from "./price";
// eslint-disable-next-line react/prop-types
function Product({title, idx}) {
    // eslint-disable-next-line react/prop-types, react/jsx-key
    let oldPrice=["10000","5000","500"];
    let newPrice=["7500","4500","300"];
    let descriptions=[["VerySuperb","intutive"],["VeryNice","Swell designed"],["VeryGood","wirless"]]
    return (
        <div className="Product" >
            <h3>{title}</h3>
            <p>{descriptions[idx][0]}</p>
            <p>{descriptions[idx][1]}</p>
            <Price oldPrice={oldPrice[idx]} newPrice={newPrice[idx]}/>
            
            
        </div>
    );
}




export default Product;
