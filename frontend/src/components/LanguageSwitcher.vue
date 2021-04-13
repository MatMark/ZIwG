<template>
  <v-menu bottom offset-y>
    <template v-slot:activator="{ on: menu }">
      <v-tooltip bottom>
        <template v-slot:activator="{ on: tooltip }">
          <v-btn
            class="mx-1"
            color="deep-purple lighten-5"
            small
            icon
            dark
            v-on="{ ...tooltip, ...menu }"
          >
            {{ selected }}
          </v-btn>
        </template>
        <span>{{ $t("appMenu.language") }}</span>
      </v-tooltip>
    </template>

    <v-list>
      <v-list-item-group v-model="item" color="primary">
        <v-list-item @click.prevent="setLocale('pl')">
          <v-list-item-icon>
            <v-img
              :src="require('@/assets/pl.svg')"
              contain
              height="15"
              width="24"
            />
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>
              PL
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click.prevent="setLocale('en')">
          <v-list-item-icon>
            <v-img
              :src="require('@/assets/en.svg')"
              contain
              height="15"
              width="24"
            />
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>
              EN
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-menu>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
const { mapActions } = createNamespacedHelpers("context");
export default {
  data: function() {
    let sel;
    if (this.$i18n.locale === "pl") {
      sel = 0;
    } else if (this.$i18n.locale === "en") sel = 1;
    else sel = 2;
    return {
      item: sel,
      selected: this.$i18n.locale
    };
  },
  methods: {
    ...mapActions(["changeLanguage"]),
    setLocale(locale) {
      this.selected = locale.toUpperCase();
      this.$i18n.locale = locale;
      this.changeLanguage(locale);
      //   location.reload();
    }
  }
};
</script>
