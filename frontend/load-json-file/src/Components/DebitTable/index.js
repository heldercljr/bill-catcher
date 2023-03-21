import React from "react"
import DataTable from "react-data-table-component"
import { useState, useEffect } from "react"
import DebitData from '../../Data/debits.json'

const columns = [
    {
      name: "CPF/CNPJ",
      selector: (row) => row.cpfcnpj,
    },
    {
      name: "Valor",
      selector: (row) => row.value,
    },
    {
      name: "Data de Vencimento",
      selector: (row) => row.due_date,
    },
    {
      name: "Código de Barras",
      selector: (row) => row.bar_code,
    },
    {
      name: "Pix Copia e Cola",
      selector: (row) => row.pix_string,
    },
    {
      name: "Tipo de Documento",
      selector: (row) => row.doc_type,
    },
  ]

function DebitTable() {
    const [data, setData] = useState([])

    const [loading, setLoading] = useState(true)
  
    useEffect(() => {
        fetchTableData()
      }, [])
    
      async function fetchTableData() {
        await fetch('http://localhost:5000', {
            method: 'get',
        });
        setLoading(false);
        const debits = DebitData
        setData(debits)
      }

      if (loading) {
        return <div>Carregando dados...</div>;
      }
    
    return(
        <div style={{ margin: "20px" }}>
        <DataTable
          title="Informações de Boletos dos usuários"
          columns={columns}
          data={data}
          loading={loading}
          pagination
        />
      </div>
    )

}

export default DebitTable;