export default {
  getGame({ commit }, genres) {
    if (genres && genres.length > 0) {
      console.log("genres: ", genres);

      genres = genres.substring(0, genres.length - 1);

      return this.$axios.$get(`/api/game?${genres}`, {
        headers: getHeaders(),
      });
      v;
    }

    return this.$axios.$get(`/api/games`, {
      headers: getHeaders(),
    });
  },

  getGameById({ commit }, id) {
    return this.$axios.$get(`/api/game/${id}`, {
      headers: getHeaders(),
    });
  },

  getCategoriesList() {
    return this.$axios.$get(`/api/categories`, {
      headers: getHeaders(),
    });
  },

  getPublishersList() {
    return this.$axios.$get(`/api/publishers`, {
      headers: getHeaders(),
    });
  },

  getPlatformsList() {
    return this.$axios.$get(`/api/platforms`, {
      headers: getHeaders(),
    });
  },

  getDevelopersList() {
    return this.$axios.$get(`/api/developers`, {
      headers: getHeaders(),
    });
  },
};

const getHeaders = () => {
  return {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
  };
};
