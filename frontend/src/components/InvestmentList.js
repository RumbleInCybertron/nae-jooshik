import React, { useEffect, useState } from 'react';
import axios from 'axios';
import InvestmentChart from './InvestmentChart';

const InvestmentList = () => {
  const [investments, setInvestments] = useState([]);
  const [selectedInvestment, setSelectedInvestment] = useState(null);

  useEffect(() => {
    axios.get('/api/investments')
      .then(response => setInvestments(response.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>내 투자</h1>
      <ul>
        {investments.map(investment => (
          <li key={investment.id} onClick={() => setSelectedInvestment(investment.id)}>
            {investment.stock_symbol} - ${investment.amount_invested}
          </li>
        ))}
      </ul>
      {selectedInvestment && <InvestmentChart investmentId={selectedInvestment} />}
    </div>
  );
};

export default InvestmentList;