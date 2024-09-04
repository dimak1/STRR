<script setup lang="ts">
import ContactDetails from '../common/ContactDetails.vue'
import FormCard from '../common/FormCard.vue'

const { t } = useTranslation()

const { userFullName } = useBcrosAccount()

const isPlatformRep = ref(true)
const hasSecondaryPlatformRep = ref(false)

const primaryResidenceRadioOptions = [{
  value: true,
  label: 'Yes'
}, {
  value: false,
  label: 'No'
}]

const onPlatformRepChange = () => {
  hasSecondaryPlatformRep.value = false
}

const handleRemoveContactDetails = () => {
  hasSecondaryPlatformRep.value = false
}

// TODO: Update this
const temp = ref(null)

</script>

<template>
  <div class="mb-20">
    <div class="mb-8">
      <URadioGroup
        id="primary-residence-radio"
        v-model="isPlatformRep"
        :options="primaryResidenceRadioOptions"
        @change="onPlatformRepChange"
      >
        <template #legend>
          <div class="font-bold mb-4 text-base">
            {{ t('platformApplication.step1.platformRepSelect') }}
          </div>
        </template>
        <template #label="{ option }">
          <div class="mb-2 text-base">
            {{ option.label }}
          </div>
        </template>
      </URadioGroup>
    </div>

    <ContactDetails
      v-if="isPlatformRep"
      :header="t('platformApplication.step1.platformRep')"
      :state="{}"
      data-test-id="platform-rep"
      show-alert-msg
    />

    <FormCard
      v-if="false"
      :header="t('platformApplication.step1.platformRep')"
      class="mb-8"
    >
      <div class="flex m:flex-col d:p-10 m:p-5">
        <!-- Left Column -->
        <div class="w-[200px]">
          <div class="mb-6 font-bold text-gray-700">
            Contact Details
          </div>
        </div>

        <!-- Right Column -->
        <div class="flex-1 space-y-6">
          <div class="text-[14px] leading-[22px]">
            {{ t('common.yourName') }}
          </div>
          <div class="mb-[16px] text-[14px] leading-[22px]">
            {{ userFullName }}
          </div>

          <div ref="testRef" class="mb-[16px] text-[14px] leading-[22px]">
            {{ t('common.disclaimerSbcConnect') }}
          </div>

          <hr>

          <UFormGroup
            name="jobTitle"
            class="mobile:mb-[16px]"
            help="Enter your current job title or position"
          >
            <UInput
              v-model="temp"
              aria-label="extension"
              placeholder="Position/Title"
            />
          </UFormGroup>

          <div class="flex flex-row justify-between w-full mb-[40px] mobile:flex-col mobile:mb-[16px] space-x-2">
            <UFormGroup name="phoneNumber" class="flex-grow mobile:mb-[16px]">
              <UInput
                v-model="temp"
                type="tel"
                aria-label="phone number"
                placeholder="Phone Number"
              />
            </UFormGroup>
            <UFormGroup name="extension" class="flex-grow">
              <UInput
                v-model="temp"
                :placeholder="t('createAccount.contactForm.extension')"
                aria-label="extension"
              />
            </UFormGroup>
          </div>

          <UInput
            v-model="temp"
            :placeholder="t('createAccount.contactForm.faxNumber')"
            aria-label="extension"
          />
          <UInput
            v-model="temp"
            :placeholder="t('createAccount.contactForm.emailAddress')"
            aria-label="extension"
          />
          <BcrosAlertsMessage :flavour="AlertsFlavourE.INFO">
            {{ t('platformApplication.step1.alertMessage') }}
          </BcrosAlertsMessage>
        </div>
      </div>
    </FormCard>

    <div
      v-if="!isPlatformRep"
      data-test-id="not-platform-rep"
    >
      <FormCard
        :header="t('platformApplication.step1.personCompletingApplication')"
        class="mb-8"
        data-test-id="person-completing-platform"
      >
        <div class="flex m:flex-col d:p-10 m:p-5">
          <!-- Left Column -->
          <div class="w-[200px]">
            <div class="mb-6 font-bold text-gray-700">
              {{ t('common.yourName') }}
            </div>
          </div>

          <!-- Right Column -->
          <div class="flex-1 space-y-6">
            <div class="mb-[16px] text-[14px] leading-[22px]">
              {{ userFullName }}
            </div>

            <div class="mb-[16px] text-[14px] leading-[22px]">
              {{ t('common.disclaimerSbcConnect') }}
            </div>
          </div>
        </div>

        <hr class="mx-10">

        <div class="flex m:flex-col d:p-10 m:p-5">
          <!-- Left Column -->
          <div class="w-[200px]">
            <div class="mb-6 font-bold text-gray-700">
              {{ t('common.contactDetails') }}
            </div>
          </div>

          <!-- Right Column -->
          <div class="flex-1 space-y-6">
            <div class="flex flex-row justify-between w-full mobile:flex-col mobile:mb-[16px] space-x-2">
              <UFormGroup name="phoneNumber" class="flex-grow mobile:mb-[16px]">
                <UInput
                  v-model="temp"
                  type="tel"
                  aria-label="phone number"
                  placeholder="Phone Number"
                />
              </UFormGroup>
              <UFormGroup name="extension" class="flex-grow">
                <UInput
                  v-model="temp"
                  :placeholder="t('createAccount.contactForm.extension')"
                  aria-label="extension"
                />
              </UFormGroup>
            </div>

            <UInput
              v-model="temp"
              :placeholder="t('createAccount.contactForm.emailAddress')"
              aria-label="extension"
            />
          </div>
        </div>
      </FormCard>

      <ContactDetails
        :header="t('platformApplication.step1.platformRep')"
        :state="{}"
        data-test-id="platform-rep"
      >
        <template #contactInfo>
          <div class="text-sm mb-10">
            This is the contact person at your organization
          </div>
        </template>
      </ContactDetails>
    </div>

    <ContactDetails
      v-if="hasSecondaryPlatformRep"
      :header="t('platformApplication.step1.secondaryPlatformRep')"
      :state="{}"
      data-test-id="secondary-platform-rep"
      show-remove-button
      @removeContactDetails="handleRemoveContactDetails()"
    >
      <template #contactInfo>
        <div class="text-sm mb-10">
          This is a back-up contact person in case the first platform representative cannot be reached
        </div>
      </template>
    </ContactDetails>

    <BcrosButtonsPrimary
      v-if="!hasSecondaryPlatformRep"
      :action="() => hasSecondaryPlatformRep = true"
      :label="t('common.addAnotherContact')"
      variant="outline"
      icon=""
      class-name="mobile:w-full mobile:mx-[0px]"
    />
  </div>
</template>

<style scoped>

</style>
