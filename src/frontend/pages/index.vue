<template>
  <div>
    <v-card color="transparent" elevation="0" class="d-flex flex-wrap mx-auto">
      <v-col>
        <div class="title_game my-14">LIST OF GAMES</div>

        <v-row align="center" justify="center">
          <div class="my-10">
          <v-row>
            <v-spacer></v-spacer>
            <FilterGame :genres="genres" @filter="povoateGames" /> 
          </v-row>
        </div>
        </v-row>

        <v-row v-if="data_by_page.length == 0 && !loading">
          <div class="title_game">No games found :c </div>
        </v-row>

        <v-row v-if="data_by_page.length == 0 && loading">
          <div class="title_game">We are loading the games... </div>
        </v-row>

        <v-row v-else align="center" justify="center">
          <CardGame
            v-for="(item, index) of data_by_page"
            :key="index"
            :game="item"
            :is-placeholder="loading"
          />
        </v-row>
        <v-row v-if="!loading" class="my-14" align="center" justify="center">
          <div class="text-center mx-auto">
            <v-pagination
              v-model="page"
              :length="quant_page"
              :total-visible="7"
            ></v-pagination>
          </div>
        </v-row>
      </v-col>
    </v-card>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import CardGame from "@/components/Game/CardGame.vue";
import FilterGame from "@/components/Game/FilterGame.vue";

export default {
  name: "IndexPage",

  components: { CardGame, FilterGame },

  data() {
    return {
      page: 1,
      page_size: 20,
      quant_page: 0,
      loading: false,

      data: [],

      genres: [],
    };
  },

  methods: {
    ...mapActions("game", ["getGame"]),

    povoateFilters(allGames) {
      for (var prop of allGames) {
        if (!this.genres.includes(prop.genre)) {
          this.genres.push(prop.genre);
        }
      }
    },

    povoateGames(genres) {
      this.loading = true;

      this.getGame(genres)
        .then((resp) => {
          this.data = [...resp];
          this.quant_page = Math.ceil(this.data.length / this.page_size);
        })
        .finally(() => {
          this.loading = false;

          this.povoateFilters(this.data);
        });
    },
  },

  created() {
    this.povoateGames();
  },

  computed: {
    data_by_page() {
      var last_item_index = this.page * this.page_size;
      return this.data.slice(last_item_index - this.page_size, last_item_index);
    },
  },
};
</script>

<style scoped>
.title_game {
  text-align: center;
  font-size: 40px !important;
}
</style>
