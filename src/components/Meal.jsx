import { useState, useEffect } from 'react';
import Food from '../assets/food.jpeg';
import { firebase } from '../firebase'; // Import the firebase instance
import { getDatabase, ref, onValue, remove } from 'firebase/database'; // Import remove function

const Meal = () => {
  const [description, setDescription] = useState(null);

  useEffect(() => {
    const fetchDataAndDelete = async () => {
      try {
        const db = getDatabase(firebase);
        const dbRef = ref(db, 'recipe'); // Get reference to 'text_data' node in Realtime Database

        onValue(dbRef, (snapshot) => {
          const textData = snapshot.val();
          if (textData) {
            setDescription(textData); // Update state only when data is fetched successfully
            deleteData(); // Delete the data after it's displayed
          }
        });
      } catch (error) {
        console.error('Error:', error);
      }
    };

    const deleteData = async () => {
      try {
        const db = getDatabase(firebase);
        const dbRef = ref(db, 'text_data'); // Get reference to 'text_data' node in Realtime Database

        remove(dbRef)
          .then(() => {
            console.log('Data deleted successfully');
          })
          .catch((error) => {
            console.error('Error deleting data:', error);
          });
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchDataAndDelete(); // Fetch data when component mounts

    // Cleanup function (optional)
    return () => {
      // Any cleanup logic can go here
    };
  }, []); // Empty dependency array ensures this effect runs only once, similar to componentDidMount in class components
  console.log(description);
  
  return (
    <div className='m--container'>
      <div className="m--title">
        {JSON.parse(description)}
      </div>
    </div>
  );
};

export default Meal;
