import React from 'react'
import { Row , Col } from 'react-bootstrap'
import Product from '../components/Product'

import products from '../products'

function HomeScreen() {
    return (
        <div>
            <h1>Latest Products</h1>
            <Row>
                {products.map(product =>(
                        <col key={product._id} sm={12} md={6} Lg={4} xl={3}>
                           <Product product = {product} /> 
                        </col>
                    ))}
            </Row>
        </div>
    )
}

export default HomeScreen