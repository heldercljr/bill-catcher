import DebitTable from "./Components/DebitTable"
import Home from "./Components/Home";
import ReactDOM  from "react-dom/client"
import { BrowserRouter, Routes, Route } from "react-router-dom";



function App() {



  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />}></Route>
      <Route path="/debits" element={<DebitTable />}>
      </Route>
    </Routes>
  </BrowserRouter>

  )
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

export default App