<template>
  <div>
    <v-card
      v-if="!isPlaceholder"
      id="card_image"
      class="ma-6 pa-0"
      width="300px"
      height="230px"
      @click="goToDetails"
    >
      <v-img :width="300" :src="game.thumbnail"></v-img>
      <div class="mt-5 px-3">
        {{ game.title }}
      </div>
    </v-card>
    <v-card v-else class="ma-6 pa-0" width="300px" height="230px">
      <v-skeleton-loader
        class="mx-auto"
        min-height="230px"
        width="300px" height="230px"
        type="image"
      ></v-skeleton-loader>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "CardGame",

  props: {
    game: {
      type: Object,
      default: () => {},
    },
    isPlaceholder: {
      type: Boolean,
      default: false,
    },
  },

  methods: {
    goToDetails() {
      this.$router.push({ path: `/details/${this.game.id}` });
    },
  },
};
</script>

<style>
#card_image:hover {
  opacity: 0.8 !important;
  cursor: pointer;
}
</style>
