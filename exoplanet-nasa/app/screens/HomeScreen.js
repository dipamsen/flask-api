import React, { Component } from "react";
import { StyleSheet, FlatList, View, Text } from "react-native";
import axios from "axios";
import { ListItem } from "react-native-elements";

export default class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      url: "http://127.0.0.1:5000/",
    };
  }
  componentDidMount() {
    this.getPlanetData();
  }
  renderItem = ({ item, index }) => (
    <ListItem
      key={index}
      onPress={() =>
        this.props.navigation.navigate("details", { planetName: item.name })
      }
    >
      <ListItem.Content>
        <ListItem.Title>{item.name}</ListItem.Title>
        <ListItem.Subtitle>{item.distance_from_earth}</ListItem.Subtitle>
      </ListItem.Content>
    </ListItem>
  );
  keyExtractor = (item, index) => index.toString();
  render() {
    return this.state.data.length == 0 ? (
      <View style={styles.container}>
        <Text>Loading Planets...</Text>
      </View>
    ) : (
      <View style={styles.container}>
        <Text>Exoplanet Catalogue</Text>
        <FlatList
          data={this.state.data}
          renderItem={this.renderItem}
          keyExtractor={this.keyExtractor}
        />
      </View>
    );
  }
  getPlanetData = () => {
    const fetchUrl = this.state.url;
    console.log(fetchUrl);
    axios
      .get(fetchUrl)
      .then((response) => {
        console.log(response.data.planets);
        this.setState({ data: response.data.planets.slice(0, 100) });
      })
      .catch((error) => {
        console.log(error);
        alert(error);
      });
  };
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "red",
    width: "100%",
  },
});
