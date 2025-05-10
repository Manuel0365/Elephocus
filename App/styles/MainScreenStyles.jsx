import { StyleSheet, Dimensions } from "react-native";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    justifyContent: "space-between",
  },
  topImage: {
    width: '100%',
    height: 200,
    marginBottom: 10, 
  },
  cardsContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 10, 
  },
  flatListContent: {
    alignItems: "center",
  },
  cardWrapper: {
    width: Dimensions.get("window").width * 1.0, 
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
    borderRadius: 20, 
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 10 },
  },
  emptyContainer: {
    justifyContent: "center",
    alignItems: "center",
    height: Dimensions.get("window").height * 0.4,
  },
});

export default styles;
