import { RegistrationTypeE } from '#imports'

export interface RegistrantI {
  firstName: string
  lastName: string
  phoneNumber: string
  extension: string
  faxNumber: string
  emailAddress: string
}
export interface PlatformRepresentativeI extends RegistrantI {
  jobTitle: string
}

export interface MailingAddressI {
  country: string
  address: string
  addressLineTwo: string
  city: string
  province: string
  postalCode: string
}

export interface BusinessDetailsI {
  legalName: string
  placeOfIncorporation: string
  businessNumber: string
  aliases: string[]
  mailingAddress: MailingAddressI
}

export interface ProviderI {
  name: string
  website: string
}

interface PlatformDetailsI {
  providers: ProviderI[]
  hasMoreThanThousandListings: boolean
}

export interface PlatformApplicationI {
  registration: {
    registrationType: RegistrationTypeE
    registrant: RegistrantI
    platformRepresentatives: PlatformRepresentativeI[]
    businessDetails: BusinessDetailsI
    platformDetails: PlatformDetailsI
  }
}
