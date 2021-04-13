<template>
  <v-app-bar app color="deep-purple darken-5" dark>
    <template v-slot:img="{ props }">
      <v-img
        v-bind="props"
        gradient="to top right, rgba(0,0,63,.7), rgba(0,63,255,.7)"
      />
    </template>
    <router-link to="/home">
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>
    </router-link>

    <v-row align="center" justify="center" class="hidden-sm-and-down">
      <v-btn-toggle tile group>
        <v-menu
          v-model="openMenu"
          transition="slide-y-transition"
          bottom
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-btn text color="deep-purple lighten-5" v-on="on">
              {{ $t("appMenu.menu") }}
              <v-icon right> mdi-chevron-down </v-icon>
            </v-btn>
          </template>

          <v-list>
            <v-list-item-group>
              <v-list-item dense :to="'/all_products'">
                <v-list-item-title>
                  {{ $t("appMenu.allProducts") }}
                </v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-menu>

        <v-btn :to="`/packing`" text color="deep-purple lighten-5">
          {{ $t("appMenu.packing") }}
        </v-btn>

        <v-btn :to="`/contact`" text color="deep-purple lighten-5">
          {{ $t("appMenu.contact") }}
        </v-btn>
      </v-btn-toggle>
    </v-row>
    <div>
      <v-toolbar class="hidden-sm-and-down" color="transparent" flat>
        <LanguageSwitcher />
      </v-toolbar>
    </div>
  </v-app-bar>
</template>

<script>
import LanguageSwitcher from "@/components/LanguageSwitcher.vue";

export default {
  components: {
    LanguageSwitcher
  },
  data() {
    return { openMenu: false };
  },
  methods: {}
};
</script>
