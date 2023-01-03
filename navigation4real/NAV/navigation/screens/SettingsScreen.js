import * as React from 'react';
import { useState , useEffect} from 'react';
import { View, Text, Button } from 'react-native';
import axios from 'axios';

export default function SettingsScreen({ navigation }) {
    const [ data, setData] = useState([]);

    const fetch = () =>{
        console.log('selam')
        axios.get ('http://127.0.0.1:8000/teacher/list-create')
        .then((res)=> setData(res.data))
        .catch(err => console.log(err))

    }
    const dele =(id) => {
        axios.delete(`http://127.0.0.1:8000/teacher/list-delete/${id}`).then(
            fetch()
        )
    }
    useEffect (()=>{
        fetch()
    },[])
    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            {/* <Text
                onPress={() => navigation.navigate('Home')}
                style={{ fontSize: 26, fontWeight: 'bold' }}>teacher Screen</Text> */}
                {/* <Text>check</Text> */}

        {data.map((item)=>{
              return <View>
                       <Text>{item.teacname}</Text>
                       <Text>{item.salary}</Text>
                       <Text>{item.department}</Text>
                       <Button 
                       title='click'
                       onPress={() => dele(item.id)}
                       />
              </View>


                })}
        </View>
    );
}
