<template>
  <v-card>
    <v-card-title>
      <!-- {{ $t('yourCartPage.stepper.yourData') }} -->
    </v-card-title>
    <v-container>
      <v-divider />
      <v-form ref="form" lazy-validation>
        <v-row>
          <v-col>
            <v-card flat>
              <v-card-title>
                {{ $t("yourCartPage.inputs.yourData.title") }}
              </v-card-title>
              <v-card-text>
                <v-text-field
                  v-model="inputs.yourData.email"
                  :rules="[rules.required, rules.email]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.yourData.email')"
                />
                <v-text-field
                  v-model="inputs.yourData.firstName"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.yourData.firstName')"
                />
                <v-text-field
                  v-model="inputs.yourData.lastName"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.yourData.lastName')"
                />
                <v-text-field
                  v-model="inputs.yourData.phone"
                  :rules="[rules.required, rules.phone]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.yourData.phone')"
                />
              </v-card-text>
            </v-card>
            <v-card flat>
              <v-card-title>
                {{ $t("yourCartPage.inputs.address.title") }}
              </v-card-title>
              <v-card-text>
                <v-radio-group v-model="inputs.address.business" row mandatory>
                  <v-radio
                    :label="$t('yourCartPage.inputs.address.private')"
                    :value="false"
                  />
                  <v-radio
                    :label="$t('yourCartPage.inputs.address.business')"
                    :value="true"
                  />
                </v-radio-group>
                <div v-if="inputs.address.business">
                  <v-text-field
                    v-model="inputs.address.businessName"
                    :rules="[rules.required]"
                    outlined
                    dense
                    :label="$t('yourCartPage.inputs.address.businessName')"
                  />
                  <v-text-field
                    v-model="inputs.address.nip"
                    :rules="[rules.required, rules.nip]"
                    outlined
                    dense
                    :label="$t('yourCartPage.inputs.address.nip')"
                  />
                </div>
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="inputs.address.street"
                      :rules="[rules.required]"
                      outlined
                      dense
                      :label="$t('yourCartPage.inputs.address.street')"
                    />
                  </v-col>
                  <v-col cols="2">
                    <v-text-field
                      v-model="inputs.address.houseNumber"
                      :rules="[rules.required]"
                      outlined
                      dense
                      :label="$t('yourCartPage.inputs.address.houseNumber')"
                    />
                  </v-col>
                  <v-col cols="2">
                    <v-text-field
                      v-model="inputs.address.apartmentNumber"
                      outlined
                      dense
                      :label="$t('yourCartPage.inputs.address.apartmentNumber')"
                    />
                  </v-col>
                </v-row>
                <v-text-field
                  v-model="inputs.address.postCode"
                  v-mask="'##-###'"
                  placeholder="xx-xxx"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.address.postCode')"
                />
                <v-text-field
                  v-model="inputs.address.city"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.address.city')"
                />
                <v-select
                  v-model="inputs.address.country"
                  :items="countries"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.address.country')"
                />
                <v-checkbox
                  v-model="inputs.address.otherSendAddress"
                  :label="$t('yourCartPage.inputs.address.otherSendAddress')"
                />
              </v-card-text>
            </v-card>
          </v-col>
          <v-col>
            <v-card v-if="inputs.address.otherSendAddress" flat>
              <v-card-title>
                {{ $t("yourCartPage.inputs.sendAddress.title") }}
              </v-card-title>
              <v-card-text>
                <v-text-field
                  v-model="inputs.sendAddress.firstName"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.sendAddress.firstName')"
                />
                <v-text-field
                  v-model="inputs.sendAddress.lastName"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.sendAddress.lastName')"
                />
                <v-text-field
                  v-model="inputs.sendAddress.phone"
                  :rules="[rules.required, rules.phone]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.sendAddress.phone')"
                />
                <v-text-field
                  v-if="inputs.address.business"
                  v-model="inputs.sendAddress.businessName"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.sendAddress.businessName')"
                />
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="inputs.sendAddress.street"
                      :rules="[rules.required]"
                      outlined
                      dense
                      :label="$t('yourCartPage.inputs.sendAddress.street')"
                    />
                  </v-col>
                  <v-col cols="2">
                    <v-text-field
                      v-model="inputs.sendAddress.houseNumber"
                      :rules="[rules.required]"
                      outlined
                      dense
                      :label="$t('yourCartPage.inputs.sendAddress.houseNumber')"
                    />
                  </v-col>
                  <v-col cols="2">
                    <v-text-field
                      v-model="inputs.sendAddress.apartmentNumber"
                      outlined
                      dense
                      :label="
                        $t('yourCartPage.inputs.sendAddress.apartmentNumber')
                      "
                    />
                  </v-col>
                </v-row>
                <v-text-field
                  v-model="inputs.sendAddress.postCode"
                  v-mask="'##-###'"
                  placeholder="xx-xxx"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.sendAddress.postCode')"
                />
                <v-text-field
                  v-model="inputs.sendAddress.city"
                  :rules="[rules.required]"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.sendAddress.city')"
                />
                <v-select
                  v-model="inputs.sendAddress.country"
                  :items="countries"
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.sendAddress.country')"
                />
              </v-card-text>
            </v-card>
            <v-card flat>
              <v-card-title>
                {{ $t("yourCartPage.inputs.additionalInfo.title") }}
              </v-card-title>
              <v-card-text>
                <v-textarea
                  v-model="inputs.additionalInfo.note"
                  counter="300"
                  maxlength="300"
                  auto-grow
                  outlined
                  dense
                  :label="$t('yourCartPage.inputs.additionalInfo.note')"
                />
                <v-checkbox v-model="regulations" :rules="[rules.required]">
                  <template v-slot:label>
                    <span>
                      {{
                        $t(
                          "yourCartPage.inputs.additionalInfo.regulationsBefore"
                        )
                      }}
                      <a target="_blank" href="/regulations" @click.stop>
                        {{
                          $t(
                            "yourCartPage.inputs.additionalInfo.regulationsLink"
                          )
                        }}
                      </a>
                      {{
                        $t(
                          "yourCartPage.inputs.additionalInfo.regulationsAfter"
                        )
                      }}
                    </span>
                  </template>
                </v-checkbox>
                <v-checkbox
                  v-model="inputs.additionalInfo.newsletter"
                  :label="$t('yourCartPage.inputs.additionalInfo.newsletter')"
                />
                <v-row style="margin-left: 5px;">
                  <span>* {{ $t("productDetailsPage.required") }}</span>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-form>
    </v-container>
    <v-card-actions>
      <v-btn tile @click="previousStep">
        {{ $t("yourCartPage.stepper.back") }}
      </v-btn>
      <v-spacer />
      <v-btn tile @click="nextStep">
        {{ $t("yourCartPage.stepper.continue") }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
const { mapGetters, mapActions } = createNamespacedHelpers("cart");
export default {
  components: {},
  data() {
    return {
      inputs: {
        yourData: {
          email: undefined,
          firstName: undefined,
          lastName: undefined,
          phone: undefined
        },
        address: {
          business: false,
          businessName: undefined,
          nip: undefined,
          street: undefined,
          houseNumber: undefined,
          apartmentNumber: undefined,
          postCode: undefined,
          city: undefined,
          country: "Polska",
          otherSendAddress: false
        },
        sendAddress: {
          firstName: undefined,
          lastName: undefined,
          phone: undefined,
          businessName: undefined,
          street: undefined,
          houseNumber: undefined,
          apartmentNumber: undefined,
          postCode: undefined,
          city: undefined,
          country: "Polska"
        },
        additionalInfo: {
          note: undefined,
          newsletter: false
        }
      },
      regulations: false,
      countries: ["Polska"],
      rules: {
        required: value =>
          !!value || this.$t("productDetailsPage.validation.notEmpty"),
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return (
            pattern.test(value) ||
            this.$t("productDetailsPage.validation.invalidEmail")
          );
        },
        phone: value => {
          const pattern = /^([+]{1}|[0]{2})[0-9]{2}[\s][0-9]{3}[\s][0-9]{3}[\s][0-9]{3}$|^([+]{1}|[0]{2})[0-9]{2}[\s][0-9]{2}[\s][0-9]{3}[\s][0-9]{2}[\s][0-9]{2}$|^([+]{1}|[0]{2})[0-9]{11}$|^[0-9]{9}$|^[0-9]{3}[\s][0-9]{3}[\s][0-9]{3}$|^[0-9]{2}[\s][0-9]{3}[\s][0-9]{2}[\s][0-9]{2}$/;
          return (
            pattern.test(value) ||
            this.$t("productDetailsPage.validation.invalidPhone")
          );
        },
        nip: value => {
          const pattern = /^[0-9]{10}$/;
          // while (value.includes('-')) {
          //   value = value.replace('-', '')
          // }
          return (
            pattern.test(value) ||
            this.$t("productDetailsPage.validation.invalidNIP")
          );
        }
      }
    };
  },
  computed: {
    ...mapGetters(["getCustomerData"])
  },
  mounted() {
    if (this.getCustomerData) {
      this.inputs = this.getCustomerData;
    }
  },
  methods: {
    ...mapActions(["changeCustomerData"]),

    nextStep() {
      if (this.$refs.form.validate()) {
        window.scrollTo({ top: 0 });
        this.changeCustomerData(this.inputs);
        this.$emit("nextStep");
      } else {
        window.scrollTo({ top: 0, behavior: "smooth" });
      }
    },
    previousStep() {
      window.scrollTo({ top: 0 });
      this.$emit("previousStep");
    }
  }
};
</script>
