import {useState, useEffect } from 'react';
import {dbService} from "firebase"

function ClockContainer() {
  const [time, setTime] = useState(new Date());
	
	const [name, setName] = useState("");
  const [names, setNames] = useState([]);
	const [date, setDate] = useState("");
  const [dates, setDates] = useState([]);
	
  const onChange = (event) => {
      const {target: {name, value}} = event;
      if (name === "name"){
        setName(name);
      } else if (name === "date"){
        setDate(value);
			}
		};
	
  const onSubmit = async (event) => {
    event.preventDefault();
		await dbSerivce.colletion("names").add({
		name,
			createdAt: Date.now(),
		})
		setName("");
	};
	
  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 1000);
    return (() => clearInterval(timer))
  }, []);
  
  return (
    <div>
      <h1>Clock</h1>
				<form onSubmit={onSubmit}>
					<input
						name = "name"
						onChange={onChange}
						value={name}
						type="text"
						placeholder="Write your name"
					/>
					<input
						name = "date"
						onChange={onChange}
						value={date}
						type="text"
						placeholder="Write your date"
					/>
					<button onSubmit={onSubmit}>Add info</button>
				</form>
			<hr />
      {/*<ul>
        { names.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
			<span>{time.toLocaleTimeString('ko-KR', {hour12:false})}</span> */}
    </div>
  )
}

export default ClockContainer;