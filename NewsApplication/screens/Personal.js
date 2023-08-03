import {View,Text, Pressable,Linking} from 'react-native';
export default function PersonalScreen(){
    return(
        <Pressable  onPress={() => Linking.openURL('http://sandythosh.netlify.app')}>
            <Text style={{color: 'blue'}}>
                Google
            </Text>
        </Pressable>
    )
}