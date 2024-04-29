import Product from "./Product.jsx";

// function ProductTab() {
//     // let options=["hitech","durable"];
    
//     // let options2={a:"hi-tech",b:"durable"};
//     return (
//         <>
//             {/* <Product title="Laptop" price="100k" features={options} /> */}
//             <Product title="Laptop" price="100k" />
//             <Product title="Bag" price={50000} />
//             <Product title="Pen" />
//         </>
//     );
// }


//activity-2

function ProductTab() {
    //for make cards in single line
    let styles={
        display:"flex",
        flexWrap:"wrap",
        justifyContent:"center",
        alignItems:"center",
    }
    return (
        <div style={styles}>
            <Product title={"Logitech"} idx={0}/>
            <Product title={"Apple Pencil"} idx={1}/>
            <Product title={"Zebaronics Keyboard"} idx={2} />
        </div>
    );
}

export default ProductTab;
