import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const InvestmentChart = ({ investmentId }) => {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    axios.get(`/api/history/?investment=${investmentId}`)
      .then(response => {
        const dates = response.data.map(record => record.date);
        const values = response.data.map(record => record.values);

        setChartData({
          labels: dates,
          datasets: [
            {
              label: 'Investment Value Over Time',
              data: values,
              borderColor: 'rgba(75,192,192,1)',
              fill: false,
            },
          ],
        });
      })
      .catch(err => console.log(err));
  }, [investmentId]);

  return (
    <div>
      <h2>투자 성과</h2>
      <Line data={chartData} />
    </div>
  );
};

export default InvestmentChart;