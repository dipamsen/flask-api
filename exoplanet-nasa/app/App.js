import React from "react";
import { StyleSheet, Text, View } from "react-native";
import HomeScreen from "./screens/HomeScreen";
import DetailsScreen from "./screens/DetailsScreen";
import { createStackNavigator } from "react-navigation-stack";
import { createAppContainer } from "react-navigation";

export default class App extends React.Component {
  render() {
    return <AppContainer />;
  }
}

const stack = createStackNavigator(
  {
    home: {
      screen: HomeScreen,
      navigationOptions: {
        headerShown: false,
      },
    },
    details: {
      screen: DetailsScreen,
    },
  },
  {
    initialRouteName: "home",
  }
);

const AppContainer = createAppContainer(stack);
