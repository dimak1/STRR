import { FormPageI } from '~/interfaces/form/form-page-i'

const steps: FormPageI[] = [
  {
    step: {
      label: 'platformApplication.stepper.step1Label',
      inactiveIconPath: '/icons/create-account/add_person.svg',
      activeIconPath: '/icons/create-account/add_person_active.svg',
      complete: false,
      isValid: false,
      alt: 'Add contact information'
    },
    title: 'platformApplication.step1.title',
    subtitle: 'platformApplication.step1.subtitle',
    formTitle: 'platformApplication.step1.primary',
    sections: []
  },
  {
    step: {
      label: 'platformApplication.stepper.step2Label',
      inactiveIconPath: '/icons/domain-add.svg',
      activeIconPath: '/icons/domain-add-active.svg',
      complete: false,
      isValid: false,
      alt: 'Add business details'
    },
    title: 'platformApplication.step2.title',
    subtitle: 'platformApplication.details.subtitle',
    formTitle: 'platformApplication.details.primary',
    sections: []
  },
  {
    step: {
      label: 'platformApplication.stepper.step3Label',
      inactiveIconPath: '/icons/aod.svg',
      activeIconPath: '/icons/aod-active.svg',
      complete: false,
      isValid: false,
      alt: 'add platform information'
    },
    title: 'platformApplication.step3.title',
    subtitle: '',
    formTitle: 'platformApplication.eligibility.primary',
    sections: []
  },
  {
    step: {
      label: 'platformApplication.stepper.step4Label',
      inactiveIconPath: '/icons/create-account/check.svg',
      activeIconPath: '/icons/create-account/check_active.svg',
      complete: false,
      isValid: false,
      alt: 'review and confirm'
    },
    title: 'platformApplication.step4.title',
    subtitle: '',
    formTitle: 'platformApplication.confirm.primary',
    sections: []
  }
]

export default steps
