<template>
  <v-dialog v-model="dialog" persistent max-width="800px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="transparent" dark v-bind="attrs" v-on="on" elevation="0">
        <v-icon class="mr-2"> mdi-filter-outline </v-icon>
        <div>Filter</div>
      </v-btn>
    </template>
    <v-card class="pa-6">
      <div class="d-flex mx-4">
        <span class="title_game">Filter</span>

        <v-spacer></v-spacer>
        <v-btn icon @click="closeModal">
          <v-icon> mdi-close </v-icon>
        </v-btn>
      </div>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-autocomplete
                v-model="selectCategorie"
                :items="categories"
                chips
                clearable
                label="Categories"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="selectYear"
                label="Year"
                class="mt-3"
                type="number"
              />
            </v-col>
            <v-col cols="12" sm="6">
              <v-autocomplete
                v-model="selectPublisher"
                :items="publishers"
                chips
                clearable
                label="Publishers"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6">
              <v-autocomplete
                v-model="selectPlataform"
                :items="plataforms"
                chips
                clearable
                label="Platforms"
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6">
              <v-autocomplete
                v-model="selectDeveloper"
                :items="developers"
                chips
                clearable
                label="Developers"
              ></v-autocomplete>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="cleanFilter"> Clean </v-btn>
        <v-btn color="blue darken-1" text @click="filterData"> Filter </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "FilterGame",

  data() {
    return {
      dialog: false,

      categories: [],
      publishers: [],
      plataforms: [],
      developers: [],

      selectCategorie: "",
      selectPublisher: "",
      selectPlataform: "",
      selectDeveloper: "",
      selectYear: -1,

      data: [
        "Skiing",
        "Ice hockey",
        "Soccer",
        "Basketball",
        "Hockey",
        "Reading",
        "Writing",
        "Coding",
        "Basejump",
      ],
    };
  },

  mounted() {
    this.getCategoriesList().then((resp) => {
      this.categories = resp;
    });

    this.getDevelopersList().then((resp) => {
      this.developers = resp;
    });

    this.getPublishersList().then((resp) => {
      this.publishers = resp;
    });

    this.getPlatformsList().then((resp) => {
      this.plataforms = resp;
    });

    this.selectYear = null;
  },

  methods: {
    ...mapActions("game", [
      "getCategoriesList",
      "getPublishersList",
      "getPlatformsList",
      "getDevelopersList",
      "getYearsList",
    ]),

    closeModal() {
      this.dialog = false
    },

    cleanFilter() {
      this.selectCategorie = "";
      this.selectPublisher = "";
      this.selectPlataform = "";
      this.selectDeveloper = "";
      this.selectYear = null;
      this.filterData()
    },

    filterData() {
      var filter = "";

      filter = this.mountFilter(filter, "category", this.selectCategorie);
      filter = this.mountFilter(filter, "developer", this.selectDeveloper);
      filter = this.mountFilter(filter, "publisher", this.selectPublisher);
      filter = this.mountFilter(filter, "platform", this.selectPlataform);
      filter = this.mountFilter(filter, "year", this.selectYear);

      this.$emit("filter", filter);
      this.closeModal()
    },

    mountFilter(currentString, currentType, currentValue) {
      if (currentValue) {
        currentString = currentString + `${currentType}=${currentValue}&`;
      }
      return currentString;
    },
  },
};
</script>

<style scoped>
.title_game {
  text-align: center;
  font-size: 30px !important;
}
</style>

