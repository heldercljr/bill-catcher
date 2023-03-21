import {Routes, Route, useNavigate} from 'react-router-dom';
import styled from 'styled-components';

const Button = styled.button`
background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;  

`
const Div1 = styled.div`
    text-align: center;
    margin-top: 500px
`

const Div2 = styled.div`
    text-align: center;
    margin-top: 50px
`
const Img = styled.img`
    margin-bottom: 200px
    margin-right: -120px
` 


function Home() {
    const navigate = useNavigate();
    const navigateToDebits = () => {
        navigate('/debits');
      };
    return(
        <div>
            <Div1><Img
                    src=
"https://uploads-ssl.webflow.com/60490db5d13c67d3ee04fd31/60490f4ea1eca408c13f9b8c_logo.svg"
                    width="300"
                    height="75"
                    className="d-inline-block align-top logo"
                    alt=""
                />

                    <Img
                    src=
"https://lh6.googleusercontent.com/MRhdLuDBV2023rMe_QA9jeyzyW81sKbN1HYKHr-slzlCbcPFumIxKJy8nQn8XTMd=w16383"
                    width="300"
                    height="75"
                    className="d-inline-block align-top logo"
                    alt=""
                />
                </Div1>
            <Div2>
                <Button className="btn btn-success" onClick={navigateToDebits}>Start</Button>
            </Div2>
                
            
        </div>
    )
}

export default Home;