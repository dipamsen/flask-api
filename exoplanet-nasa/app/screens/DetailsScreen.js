import React, { Component } from "react";
import { View, Text } from "react-native";
import axios from "axios";
import { Card, Icon, Button } from "react-native-elements";

export default class Details extends Component {
  constructor(props) {
    super(props);
    this.state = {
      details: {},
      // @ts-ignore
      imagePath: require("../assets/gas_giant.png"),
      url: `http://127.0.0.1:5000/planet?name=${this.props.navigation.getParam(
        "planetName"
      )}`,
      planetName: "",
    };
  }
  componentDidMount() {
    this.getDetails();
  }
  setDetails = (planetDetails) => {
    const planetType = planetDetails.planet_type;
    let imagePath = "";
    switch (planetType.toLowerCase()) {
      case "gas giant":
        // @ts-ignore
        imagePath = require("../assets/gas_giant.png");
        break;
      case "terrestrial":
        // @ts-ignore
        imagePath = require("../assets/terrestrial.png");
        break;
      case "neptune like":
        // @ts-ignore
        imagePath = require("../assets/neptune_like.png");
        break;
      case "super earth":
        // @ts-ignore
        imagePath = require("../assets/super_earth.png");
        break;
      default:
        // @ts-ignore
        imagePath = require("../assets/gas_giant.png");
        break;
    }
    this.setState({ imagePath, details: planetDetails });
  };
  getDetails = () => {
    axios
      .get(this.state.url)
      .then((response) => {
        this.setDetails(response.data.data);
      })
      .catch((err) => alert(err));
  };
  render() {
    const { details, imagePath } = this.state;
    if (details.specifications) {
      return (
        <View>
          <Card>
            <Card.Title>{details.name}</Card.Title>
            <Card.Image source={imagePath}></Card.Image>
            <View>
              <Text>Distance from Earth: {details.distance_from_earth}</Text>
              <Text>Distance from Sun: {details.distance_from_sun}</Text>
              <Text>Gravity: {details.gravity}</Text>
              <Text>Orbital Period: {details.orbital_period}</Text>
              <Text>Orbital Speed: {details.orbital_speed}</Text>
              <Text>Planet Mass: {details.planet_mass}</Text>
              <Text>Planet Radius: {details.planet_radius}</Text>
              <Text>Planet Type: {details.planet_type}</Text>
            </View>
            <View>
              <Text>{details.specifications ? "Specifications: " : ""}</Text>
              {details.specifications.map((item, index) => (
                <Text key={index.toString()}>• {item}</Text>
              ))}
            </View>
          </Card>
        </View>
      );
    } else {
      return (
        <View>
          <Text>Loading...</Text>
        </View>
      );
    }
  }
}
